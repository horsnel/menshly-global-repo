(function(){
  // Back to top
  var btn=document.getElementById("backToTop");
  window.addEventListener("scroll",function(){btn.style.display=window.scrollY>300?"block":"none"});
  btn.addEventListener("click",function(){window.scrollTo({top:0,behavior:"smooth"})});

  // Dark mode toggle
  (function(){
    var toggle=document.getElementById("theme-toggle");
    if(!toggle)return;
    var saved=localStorage.getItem("theme");
    if(saved){document.documentElement.setAttribute("data-theme",saved)}
    else if(window.matchMedia&&window.matchMedia("(prefers-color-scheme:dark)").matches){
      document.documentElement.setAttribute("data-theme","dark");
    }
    toggle.addEventListener("click",function(){
      var current=document.documentElement.getAttribute("data-theme");
      var next=current==="dark"?"light":"dark";
      document.documentElement.setAttribute("data-theme",next);
      localStorage.setItem("theme",next);
    });
  })();

  // Header date - full professional format
  (function(){
    var dateEl=document.getElementById("headerDate");
    if(!dateEl)return;
    function update(){
      var now=new Date();
      var days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
      var months=["January","February","March","April","May","June","July","August","September","October","November","December"];
      var day=days[now.getDay()];
      var mon=months[now.getMonth()];
      var date=now.getDate();
      var year=now.getFullYear();
      dateEl.textContent=day+', '+mon+' '+date+', '+year;
    }
    update();
    setInterval(update,60000);
  })();

  // Cookie consent
  var cc=localStorage.getItem("cookie_consent");
  if(cc==="accepted"&&typeof gtag==="function"){gtag("consent","update",{analytics_storage:"granted"})}

  // Reading progress bar (article pages only)
  (function(){
    var bar = document.getElementById("reading-progress-bar");
    if (!bar) return;
    var article = bar.closest(".post-page") || bar.closest("article");
    if (!article) return;
    window.addEventListener("scroll", function(){
      var rect = article.getBoundingClientRect();
      var articleTop = rect.top + window.scrollY;
      var articleHeight = article.scrollHeight;
      var scrolled = window.scrollY - articleTop + window.innerHeight * 0.3;
      var progress = Math.max(0, Math.min(100, (scrolled / articleHeight) * 100));
      bar.style.width = progress + "%";
    });
  })();

  // Sticky masthead on scroll
  (function(){
    var sticky = document.getElementById("masthead-sticky");
    if (!sticky) return;
    window.addEventListener("scroll", function(){
      if (window.scrollY > 250) {
        sticky.classList.add("visible");
      } else {
        sticky.classList.remove("visible");
      }
    });
  })();

  // Subscribe dropdown
  (function(){
    var toggle = document.getElementById("subscribe-toggle");
    var dropdown = document.getElementById("subscribe-dropdown");
    if (!toggle || !dropdown) return;
    toggle.addEventListener("click", function(e){
      e.stopPropagation();
      dropdown.classList.toggle("active");
    });
    document.addEventListener("click", function(e){
      if (!dropdown.contains(e.target) && e.target !== toggle) {
        dropdown.classList.remove("active");
      }
    });
    // Handle form submission
    var form = document.getElementById("mastheadNlForm");
    if (form) {
      form.addEventListener("submit", function(e){
        e.preventDefault();
        var email = form.querySelector('input[type="email"]');
        var btn = form.querySelector('button');
        var fd = new FormData(form);
        fetch(form.action, {method:'POST', body:fd, headers:{'Accept':'application/json'}})
        .then(function(r){
          if(r.ok){
            btn.textContent = 'Subscribed!';
            btn.style.background = '#27ae60';
            email.value = '';
            setTimeout(function(){ btn.textContent = 'Subscribe Free \u2192'; btn.style.background = ''; }, 3000);
          }
        }).catch(function(){});
      });
    }
  })();

  // Mobile nav toggle
  (function(){
    var menuToggle = document.getElementById("menu-toggle");
    var navBar = document.getElementById("nav-bar");
    if (!menuToggle || !navBar) return;
    menuToggle.addEventListener("click", function(){
      navBar.classList.toggle("mobile-open");
    });
  })();

  // Exit intent modal (desktop only)
  (function(){
    var modal = document.getElementById("exitIntentModal");
    var closeBtn = document.getElementById("exitIntentClose");
    if (!modal) return;
    var shown = localStorage.getItem("exit_intent_shown");
    if (shown) return;
    document.addEventListener("mouseout", function(e){
      if (e.clientY < 5 && !localStorage.getItem("exit_intent_shown")) {
        modal.classList.add("active");
        localStorage.setItem("exit_intent_shown", "1");
      }
    });
    if (closeBtn) {
      closeBtn.addEventListener("click", function(){
        modal.classList.remove("active");
      });
    }
    modal.addEventListener("click", function(e){
      if (e.target === modal) modal.classList.remove("active");
    });
  })();

  // Mobile subscribe bar dismiss
  (function(){
    var bar = document.getElementById("mobileSubscribeBar");
    var dismiss = document.getElementById("mobileSubscribeDismiss");
    if (!bar || !dismiss) return;
    var dismissed = localStorage.getItem("mobile_sub_dismissed");
    if (dismissed) { bar.style.display = "none"; return; }
    dismiss.addEventListener("click", function(){
      bar.style.display = "none";
      localStorage.setItem("mobile_sub_dismissed", "1");
    });
  })();

  // Breaking news dynamic loader
  (function(){
    var alert = document.getElementById("breaking-alert");
    if (!alert) return;
    var existingText = alert.querySelector(".breaking-alert-text");
    if (existingText && existingText.textContent.trim()) return;
    fetch("/api/breaking-news", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "get" })
    }).then(function(r){ return r.json(); }).then(function(data){
      if (!data.active || !data.headline) return;
      if (localStorage.getItem("breaking_dismissed")) return;
      alert.style.display = "";
      var badge = alert.querySelector(".breaking-alert-badge");
      var textEl = alert.querySelector(".breaking-alert-text");
      if (textEl) textEl.textContent = data.headline;
      if (data.link) {
        alert.style.cursor = "pointer";
        alert.addEventListener("click", function(){
          window.open(data.link, "_blank");
        });
      }
      var closeBtn = document.getElementById("breaking-alert-close");
      if (closeBtn) {
        closeBtn.addEventListener("click", function(e){
          e.stopPropagation();
          alert.style.display = "none";
          localStorage.setItem("breaking_dismissed", "1");
        });
      }
    }).catch(function(){});
  })();

  // Handle all newsletter forms
  document.querySelectorAll('.nl-form').forEach(function(form){
    if (form.dataset.bound) return;
    form.dataset.bound = '1';
    // Skip if already handled (masthead form)
    if (form.id === 'mastheadNlForm') return;
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var email = form.querySelector('input[type="email"]');
      var btn = form.querySelector('button');
      if (!email || !email.value) return;
      var fd = new FormData(form);
      fetch(form.action, {method:'POST', body:fd, headers:{'Accept':'application/json'}})
      .then(function(r){
        if(r.ok){
          if (btn) { btn.textContent = 'Subscribed!'; btn.style.background = '#27ae60'; }
          email.value = '';
          setTimeout(function(){ if(btn){ btn.textContent = 'Subscribe Free \u2192'; btn.style.background = ''; } }, 3000);
        }
      }).catch(function(){});
    });
  });
})();
