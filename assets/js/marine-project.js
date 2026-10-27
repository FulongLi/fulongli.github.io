/* Right-hand contents and current-section tracking, using the site's gutter. */
(function () {
  var contents = document.querySelector('.project-contents');
  if (!contents) return;
  var article = document.querySelector('.page__content');
  var main = document.getElementById('main');
  var masthead = document.querySelector('.masthead');
  var desktop = window.matchMedia('(min-width: 1200px)');
  var sections = Array.from(contents.querySelectorAll('a[href^="#"]')).map(function (link) {
    return { link: link, heading: document.getElementById(link.hash.slice(1)) };
  }).filter(function (section) { return section.heading; });
  var activeLink;
  var framePending = false;

  function headerOffset() {
    return masthead ? masthead.getBoundingClientRect().height : 0;
  }

  function updateContents() {
    framePending = false;
    var offset = headerOffset() + 24;
    var mainRect = main.getBoundingClientRect();
    var left = article.getBoundingClientRect().right + 12;
    var right = document.documentElement.clientWidth - 8;
    var width = right - left;
    var sidebar = desktop.matches && width >= 160;
    contents.classList.toggle('is-sidebar', sidebar);
    if (sidebar) {
      contents.style.setProperty('--contents-left', left + 'px');
      contents.style.setProperty('--contents-width', width + 'px');
      contents.style.setProperty('--contents-top', offset + 'px');
      // Stop alongside the end of the article instead of covering the footer.
      var top = Math.min(offset, mainRect.bottom - contents.getBoundingClientRect().height - 24);
      contents.style.setProperty('--contents-top', top + 'px');
    } else {
      contents.style.removeProperty('--contents-left');
      contents.style.removeProperty('--contents-width');
      contents.style.removeProperty('--contents-top');
    }

    var current = sections[0];
    var activationLine = Math.max(offset, sections.length ? parseFloat(getComputedStyle(sections[0].heading).scrollMarginTop) || 0 : 0) + 4;
    sections.forEach(function (section) {
      if (section.heading.getBoundingClientRect().top <= activationLine) current = section;
    });
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2) {
      current = sections[sections.length - 1];
    }
    if (current && current.link !== activeLink) {
      if (activeLink) activeLink.removeAttribute('aria-current');
      current.link.setAttribute('aria-current', 'location');
      activeLink = current.link;
      if (sidebar) {
        var linkRect = activeLink.getBoundingClientRect();
        var navRect = contents.getBoundingClientRect();
        if (linkRect.top < navRect.top || linkRect.bottom > navRect.bottom) {
          contents.scrollTop += linkRect.top - navRect.top - navRect.height / 2;
        }
      }
    }
  }

  function scheduleUpdate() {
    if (framePending) return;
    framePending = true;
    window.requestAnimationFrame(updateContents);
  }

  contents.addEventListener('click', function (event) {
    var link = event.target.closest('a[href^="#"]');
    if (!link || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    var target = document.getElementById(link.hash.slice(1));
    if (!target) return;
    event.preventDefault();
    event.stopPropagation();
    var offset = headerOffset();
    window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - offset - 24, behavior: 'auto' });
    if (window.location.hash !== link.hash) history.pushState(null, '', link.hash);
    target.setAttribute('tabindex', '-1');
    target.focus({ preventScroll: true });
    scheduleUpdate();
  }, true);

  window.addEventListener('scroll', scheduleUpdate, { passive: true });
  window.addEventListener('resize', scheduleUpdate, { passive: true });
  window.addEventListener('hashchange', scheduleUpdate);
  window.addEventListener('pageshow', scheduleUpdate);
  document.addEventListener('load', scheduleUpdate, true);
  if ('ResizeObserver' in window) {
    var observer = new ResizeObserver(scheduleUpdate);
    observer.observe(main);
    if (masthead) observer.observe(masthead);
  }
  updateContents();
}());
