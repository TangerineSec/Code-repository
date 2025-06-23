<template>
  <div class="app-container">
    <header class="main-header">
      <div class="logo">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm3.61 6.39c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zm-8.22 0c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zm4.61 9.72c-1.85 0-3.44-1.12-4.13-2.72h8.26c-.69 1.6-2.28 2.72-4.13 2.72z" fill="white"/>
</svg>
        <div class="logo-text">
          <span>CATCATCAT</span>
          <span class="subtitle">CATCAT-CAT</span>
        </div>
      </div>
      <div class="user-info">
        欢迎登录 | 中心认证平台
      </div>
    </header>

    <main class="content-body">
      <LoginForm />
    </main>
    
    <div class="background-lines"></div>
    <div class="city-skyline"></div>

    <footer class="main-footer-bottom">
      Copyright 2023-2024 中国橘子公司 All Rights Reserved.
    </footer>
  </div>
</template>

<script setup>
import LoginForm from './components/LoginForm.vue';
</script>

<style>
/* Global Styles */
body {
  margin: 0;
  font-family: 'Noto Sans SC', sans-serif;
  background-color: #003366;
  color: #fff;
  overflow: hidden; /* Prevents scrollbars from background elements */
}

#app {
  height: 100vh;
  width: 100vw;
}

.app-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  position: relative;
  z-index: 1;
}

/* Header */
.main-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 50px;
  background-color: #004a99; /* Slightly lighter blue */
  flex-shrink: 0;
}

.logo {
  display: flex;
  align-items: center;
}

.logo-text {
  display: flex;
  flex-direction: column;
  margin-left: 15px;
}

.logo-text .subtitle {
  font-size: 0.75rem;
  opacity: 0.8;
}

.user-info {
  font-size: 1rem;
}

/* Main Content */
.content-body {
  flex-grow: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Background Decorations */
.background-lines {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.05) 1px, transparent 1px);
  background-size: 50px 50px;
  opacity: 0.5;
  z-index: -2;
}

.city-skyline {
    position: absolute;
    bottom: 50px; /* Position it above the footer */
    left: 0;
    width: 100%;
    height: 100px;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 120'%3E%3Cpath fill='%23002244' fill-opacity='0.8' d='M0,120L60,110.7C120,101,240,83,360,74.7C480,66,600,66,720,80C840,94,960,123,1080,126.7C1200,130,1320,108,1380,97.3L1440,86.7L1440,120L1380,120C1320,120,1200,120,1080,120C960,120,840,120,720,120C600,120,480,120,360,120C240,120,120,120,60,120L0,120Z'%3E%3C/path%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-size: cover;
    z-index: -1;
}


/* Footer */
.main-footer-bottom {
  text-align: center;
  padding: 15px;
  font-size: 0.8rem;
  background-color: rgba(0, 0, 0, 0.2);
  position: absolute;
  bottom: 0;
  width: 100%;
}
</style>
