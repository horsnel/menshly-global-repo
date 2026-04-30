/**
 * MENSHLY GLOBAL — Interactive Features
 * Reading Progress, Scroll Animations, Dark Mode, Copy Code, Card Tilt, Stats Counter, ToC
 */
(function () {
  'use strict';

  // ============================================
  // READING PROGRESS BAR
  // ============================================
  function initReadingProgress() {
    var bar = document.getElementById('readingProgress');
    if (!bar) return;

    // Only show on article pages
    var articleContent = document.querySelector('.article-content');
    if (!articleContent) { bar.style.display = 'none'; return; }

    function updateProgress() {
      var scrollTop = window.scrollY;
      var docHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (docHeight <= 0) { bar.style.width = '0%'; return; }
      var progress = Math.min((scrollTop / docHeight) * 100, 100);
      bar.style.width = progress + '%';
    }

    window.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();
  }

  // ============================================
  // SCROLL-TRIGGERED REVEAL ANIMATIONS
  // ============================================
  function initScrollReveal() {
    var revealTargets = '.article-card, .playbook-card, .tool-card, .hiw-step, .process-step, .section-header, .newsletter-inner, .story-box';

    // Add reveal class to all targets
    var elements = document.querySelectorAll(revealTargets);
    elements.forEach(function (el, i) {
      el.classList.add('reveal-element');
      // Stagger cards in grids
      if (el.classList.contains('article-card') || el.classList.contains('playbook-card') || el.classList.contains('tool-card')) {
        var parent = el.parentElement;
        if (parent) {
          var siblings = Array.from(parent.children).filter(function (c) {
            return c.classList.contains('article-card') || c.classList.contains('playbook-card') || c.classList.contains('tool-card');
          });
          var idx = siblings.indexOf(el);
          el.style.transitionDelay = (idx * 80) + 'ms';
        }
      }
    });

    // Hero elements animate in immediately
    var heroEls = document.querySelectorAll('.hero-badge, .hero-title, .hero-desc, .hero-buttons, .stats-bar');
    heroEls.forEach(function (el, i) {
      el.classList.add('reveal-element', 'revealed');
      el.style.transitionDelay = (i * 100) + 'ms';
    });

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    elements.forEach(function (el) { observer.observe(el); });
  }

  // ============================================
  // ANIMATED STATS COUNTER
  // ============================================
  function initStatsCounter() {
    var statsNumbers = document.querySelectorAll('.stats-number[data-count]');
    if (!statsNumbers.length) return;

    var observed = false;
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting && !observed) {
          observed = true;
          statsNumbers.forEach(function (el) {
            var target = parseInt(el.dataset.count, 10);
            var suffix = el.dataset.suffix || '';
            var duration = 1500;
            var start = 0;
            var startTime = null;

            function animate(timestamp) {
              if (!startTime) startTime = timestamp;
              var progress = Math.min((timestamp - startTime) / duration, 1);
              // Ease out cubic
              var eased = 1 - Math.pow(1 - progress, 3);
              var current = Math.floor(eased * target);
              el.textContent = current + suffix;
              if (progress < 1) requestAnimationFrame(animate);
              else el.textContent = target + suffix;
            }

            requestAnimationFrame(animate);
          });
          observer.disconnect();
        }
      });
    }, { threshold: 0.5 });

    statsNumbers.forEach(function (el) { observer.observe(el); });
  }

  // ============================================
  // DARK MODE TOGGLE
  // ============================================
  function initDarkMode() {
    var toggle = document.getElementById('darkModeToggle');
    if (!toggle) return;

    // Check saved preference or system preference
    var saved = localStorage.getItem('mg_dark_mode');
    if (saved === 'true' || (saved === null && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.setAttribute('data-theme', 'dark');
      toggle.classList.add('active');
    }

    toggle.addEventListener('click', function () {
      var isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      if (isDark) {
        document.documentElement.removeAttribute('data-theme');
        toggle.classList.remove('active');
        localStorage.setItem('mg_dark_mode', 'false');
      } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        toggle.classList.add('active');
        localStorage.setItem('mg_dark_mode', 'true');
      }
    });
  }

  // ============================================
  // COPY CODE BLOCKS
  // ============================================
  function initCopyCode() {
    var codeBlocks = document.querySelectorAll('.article-content pre');
    codeBlocks.forEach(function (block) {
      var btn = document.createElement('button');
      btn.className = 'code-copy-btn';
      btn.textContent = 'COPY';
      btn.setAttribute('aria-label', 'Copy code');
      block.style.position = 'relative';
      block.appendChild(btn);

      btn.addEventListener('click', function () {
        var code = block.querySelector('code');
        var text = code ? code.textContent : block.textContent;
        navigator.clipboard.writeText(text).then(function () {
          btn.textContent = 'COPIED!';
          btn.classList.add('copied');
          setTimeout(function () {
            btn.textContent = 'COPY';
            btn.classList.remove('copied');
          }, 2000);
        });
      });
    });
  }

  // ============================================
  // 3D CARD TILT EFFECT
  // ============================================
  function initCardTilt() {
    // Only on desktop
    if (window.matchMedia('(hover: none)').matches) return;

    var cards = document.querySelectorAll('.article-card, .playbook-card');
    cards.forEach(function (card) {
      card.addEventListener('mousemove', function (e) {
        var rect = card.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;
        var centerX = rect.width / 2;
        var centerY = rect.height / 2;
        var rotateX = ((y - centerY) / centerY) * -3;
        var rotateY = ((x - centerX) / centerX) * 3;

        card.style.transform = 'perspective(800px) rotateX(' + rotateX + 'deg) rotateY(' + rotateY + 'deg) scale(1.02)';
        card.style.transition = 'transform 0.1s ease';
      });

      card.addEventListener('mouseleave', function () {
        card.style.transform = 'perspective(800px) rotateX(0) rotateY(0) scale(1)';
        card.style.transition = 'transform 0.4s ease';
      });
    });
  }

  // ============================================
  // TABLE OF CONTENTS (Article Pages)
  // ============================================
  function initTableOfContents() {
    var articleContent = document.querySelector('.article-content');
    var tocContainer = document.getElementById('tocContainer');
    if (!articleContent || !tocContainer) return;

    var headings = articleContent.querySelectorAll('h2, h3');
    if (headings.length < 2) { tocContainer.style.display = 'none'; return; }

    // Build ToC list
    var tocList = document.createElement('ul');
    tocList.className = 'toc-list';
    var currentH2 = null;

    headings.forEach(function (heading, i) {
      // Add ID to heading if not present
      if (!heading.id) {
        heading.id = 'heading-' + i;
      }

      var li = document.createElement('li');
      li.className = 'toc-item toc-' + heading.tagName.toLowerCase();
      var a = document.createElement('a');
      a.href = '#' + heading.id;
      a.textContent = heading.textContent;
      a.className = 'toc-link';
      li.appendChild(a);
      tocList.appendChild(li);
    });

    tocContainer.appendChild(tocList);

    // Mobile toggle
    var tocToggle = document.getElementById('tocToggle');
    if (tocToggle) {
      tocToggle.addEventListener('click', function () {
        tocContainer.classList.toggle('toc-open');
        var icon = tocToggle.querySelector('.toc-toggle-icon');
        if (icon) icon.textContent = tocContainer.classList.contains('toc-open') ? '−' : '+';
      });
    }

    // Active scroll tracking
    var tocLinks = tocList.querySelectorAll('.toc-link');
    var headingPositions = [];
    headings.forEach(function (h) {
      headingPositions.push({ id: h.id, top: h.offsetTop });
    });

    function updateActiveHeading() {
      var scrollTop = window.scrollY + 120;
      var activeId = '';
      for (var i = headingPositions.length - 1; i >= 0; i--) {
        if (scrollTop >= headingPositions[i].top) {
          activeId = headingPositions[i].id;
          break;
        }
      }
      tocLinks.forEach(function (link) {
        link.classList.remove('toc-active');
        if (link.getAttribute('href') === '#' + activeId) {
          link.classList.add('toc-active');
        }
      });
    }

    window.addEventListener('scroll', updateActiveHeading, { passive: true });
    updateActiveHeading();
  }

  // ============================================
  // BOOKMARK / SAVE ARTICLES
  // ============================================
  function initBookmark() {
    var bookmarkBtn = document.getElementById('bookmarkBtn');
    if (!bookmarkBtn) return;

    var BOOKMARKS_KEY = 'menshly_bookmarks';
    var pagePath = window.location.pathname;

    function getBookmarks() {
      try { return JSON.parse(localStorage.getItem(BOOKMARKS_KEY) || '[]'); }
      catch { return []; }
    }

    function isBookmarked() {
      return getBookmarks().indexOf(pagePath) !== -1;
    }

    function setBookmarked(bookmarked) {
      var bookmarks = getBookmarks();
      if (bookmarked) {
        if (bookmarks.indexOf(pagePath) === -1) bookmarks.push(pagePath);
      } else {
        bookmarks = bookmarks.filter(function (p) { return p !== pagePath; });
      }
      localStorage.setItem(BOOKMARKS_KEY, JSON.stringify(bookmarks));
    }

    // Init state
    if (isBookmarked()) {
      bookmarkBtn.classList.add('bookmarked');
      var icon = bookmarkBtn.querySelector('.bookmark-icon');
      if (icon) icon.setAttribute('fill', 'currentColor');
    }

    bookmarkBtn.addEventListener('click', function () {
      var wasBookmarked = isBookmarked();
      setBookmarked(!wasBookmarked);
      var icon = bookmarkBtn.querySelector('.bookmark-icon');

      if (wasBookmarked) {
        bookmarkBtn.classList.remove('bookmarked');
        if (icon) icon.setAttribute('fill', 'none');
      } else {
        bookmarkBtn.classList.add('bookmarked');
        if (icon) icon.setAttribute('fill', 'currentColor');
        // Pop animation
        bookmarkBtn.classList.add('like-pop');
        setTimeout(function () { bookmarkBtn.classList.remove('like-pop'); }, 400);
      }
    });
  }

  // ============================================
  // SHARE BUTTONS
  // ============================================
  function initShareButtons() {
    var shareContainer = document.getElementById('shareButtons');
    if (!shareContainer) return;

    var url = encodeURIComponent(window.location.href);
    var title = encodeURIComponent(document.title);
    var text = encodeURIComponent('Check out this article on Menshly Global:');

    shareContainer.querySelector('.share-whatsapp').href = 'https://wa.me/?text=' + text + '%20' + url;
    shareContainer.querySelector('.share-twitter').href = 'https://twitter.com/intent/tweet?text=' + text + '&url=' + url;
    shareContainer.querySelector('.share-linkedin').href = 'https://www.linkedin.com/sharing/share-offsite/?url=' + url;

    var copyLink = shareContainer.querySelector('.share-copy');
    if (copyLink) {
      copyLink.addEventListener('click', function (e) {
        e.preventDefault();
        navigator.clipboard.writeText(window.location.href).then(function () {
          var orig = copyLink.querySelector('.share-label');
          if (orig) {
            var saved = orig.textContent;
            orig.textContent = 'COPIED!';
            setTimeout(function () { orig.textContent = saved; }, 2000);
          }
        });
      });
    }
  }

  // ============================================
  // HEART BURST PARTICLES
  // ============================================
  function initHeartBurst() {
    window.createHeartBurst = function (button) {
      var hearts = ['❤', '♥', '💛', '🔥'];
      for (var i = 0; i < 8; i++) {
        var heart = document.createElement('span');
        heart.className = 'heart-particle';
        heart.textContent = hearts[Math.floor(Math.random() * hearts.length)];
        heart.style.left = (Math.random() * 100) + '%';
        heart.style.animationDelay = (Math.random() * 0.3) + 's';
        heart.style.fontSize = (12 + Math.random() * 10) + 'px';
        button.appendChild(heart);
        (function (h) {
          setTimeout(function () { h.remove(); }, 1000);
        })(heart);
      }
    };
  }

  // ============================================
  // INIT ALL
  // ============================================
  function init() {
    initReadingProgress();
    initScrollReveal();
    initStatsCounter();
    initDarkMode();
    initCopyCode();
    initCardTilt();
    initTableOfContents();
    initBookmark();
    initShareButtons();
    initHeartBurst();
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
