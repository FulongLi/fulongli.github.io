/* Keep the case-study headings clear of the site's sticky masthead. */
(function () {
  var contents = document.querySelector('.project-contents');
  if (!contents) return;
  contents.addEventListener('click', function (event) {
    var link = event.target.closest('a[href^="#"]');
    if (!link || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    var target = document.getElementById(link.hash.slice(1));
    if (!target) return;
    event.preventDefault();
    event.stopPropagation();
    var masthead = document.querySelector('.masthead');
    var offset = masthead ? masthead.getBoundingClientRect().height : 0;
    window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - offset - 24, behavior: 'auto' });
    history.pushState(null, '', link.hash);
    target.setAttribute('tabindex', '-1');
    target.focus({ preventScroll: true });
  }, true);
}());
