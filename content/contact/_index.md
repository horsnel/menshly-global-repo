---
title: "Contact Us"
date: 2026-04-24
badge: "CONTACT"
---

## Get In Touch

Have a question about one of our opportunities, playbooks, or tools? Want to partner with us? Have a startup story you want to share? We read every message and respond within 48 hours.

## Send Us a Message

<div class="contact-form">
  <form onsubmit="submitContact(event)">
    <div class="form-group">
      <label>Your Name</label>
      <input type="text" class="input-brutal" placeholder="JOHN DOE" required>
    </div>
    <div class="form-group">
      <label>Your Email</label>
      <input type="email" class="input-brutal" placeholder="JOHN@EXAMPLE.COM" required>
    </div>
    <div class="form-group">
      <label>Subject</label>
      <input type="text" class="input-brutal" placeholder="WHAT'S THIS ABOUT?" required>
    </div>
    <div class="form-group">
      <label>Message</label>
      <textarea class="input-brutal" placeholder="TELL US WHAT'S ON YOUR MIND..." rows="5" required></textarea>
    </div>
    <button type="submit" class="btn-brutal btn-yellow" style="width:100%;justify-content:center;">SEND MESSAGE</button>
  </form>
</div>

## Other Ways to Reach Us

<div class="contact-grid">
  <div class="contact-info-card">
    <h3>General Inquiries</h3>
    <p>hello@menshlyglobal.com</p>
  </div>
  <div class="contact-info-card">
    <h3>Partnerships</h3>
    <p>partners@menshlyglobal.com</p>
  </div>
  <div class="contact-info-card">
    <h3>Playbook Support</h3>
    <p>support@menshlyglobal.com</p>
  </div>
  <div class="contact-info-card">
    <h3>Press & Media</h3>
    <p>press@menshlyglobal.com</p>
  </div>
</div>

## Community

Join thousands of AI entrepreneurs and builders who are turning artificial intelligence into real revenue. Follow us on social media for daily insights, new opportunity alerts, and behind-the-scenes looks at how real AI businesses operate.

<script>
function submitContact(e) {
  e.preventDefault();
  const form = e.target;
  const btn = form.querySelector('button');
  btn.textContent = 'MESSAGE SENT!';
  btn.style.background = 'var(--black)';
  btn.style.color = 'var(--white)';
  setTimeout(() => {
    form.reset();
    btn.textContent = 'SEND MESSAGE';
    btn.style.background = '';
    btn.style.color = '';
  }, 3000);
}
</script>
