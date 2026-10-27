/* Optional remote services must not hold the document's load event open. */
(function () {
  var needsMath = document.currentScript.getAttribute('data-mathjax') === 'true';

  function loadScript(src) {
    var script = document.createElement('script');
    script.async = true;
    script.src = src;
    document.head.appendChild(script);
  }

  function startServices() {
    if (document.getElementById('busuanzi_value_site_pv')) {
      loadScript('https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js');
    }
    if (needsMath) {
      loadScript('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML');
    }
  }

  function afterLoad() {
    // A new task lets the load event finish before adding remote dependencies.
    window.setTimeout(startServices, 0);
  }

  if (document.readyState === 'complete') {
    afterLoad();
  } else {
    window.addEventListener('load', afterLoad, { once: true });
  }
}());
