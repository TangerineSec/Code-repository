<template>
  <div class="login-card">
    <!-- Left Side: Dark Form -->
    <div class="form-section">
      <div class="form-group">
        <label for="username">账号</label>
        <div class="input-wrapper">
           <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
           <input type="text" id="username" v-model="form.username" placeholder="admin">
        </div>
      </div>
      <div class="form-group">
        <label for="password">密码</label>
         <div class="input-wrapper">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
            <input type="password" id="password" v-model="form.password" placeholder="请输入密码">
        </div>
      </div>
      <div class="form-group">
        <label for="captcha">验证码</label>
        <div class="captcha-wrapper">
          <input type="text" id="captcha" v-model="form.captcha" placeholder="请输入">
          <img :src="captchaUrl" @click="fetchCaptcha" class="captcha-image" alt="Captcha">
        </div>
      </div>
      <button class="login-button" @click="handleLogin">登录</button>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>

    <!-- Right Side: Illustration -->
    <div class="illustration-section">
      <div class="illustration-content">
          <h2>遇见是最大的幸运</h2>
          <p>壹生贰,，贰生叁，叁生万物</p>
          <div class="illustration-image">
            <img src="/src/assets/illustration.svg" alt="Tech Illustration" />
          </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

// Backend API URL
const API_URL = 'http://127.0.0.1:5001';

const form = ref({
  username: 'admin',
  password: '',
  captcha: ''
});

const captchaUrl = ref('');
const errorMessage = ref('');

const fetchCaptcha = async () => {
  try {
    // Add a timestamp to prevent browser caching
    const response = await axios.get(`${API_URL}/api/captcha?t=${new Date().getTime()}`, {
      responseType: 'blob'
    });
    captchaUrl.value = URL.createObjectURL(response.data);
    errorMessage.value = ''; // Clear previous errors
  } catch (error) {
    console.error('Failed to fetch captcha:', error);
    errorMessage.value = '无法加载验证码。';
  }
};

const handleLogin = async () => {
  if (!form.value.username || !form.value.password || !form.value.captcha) {
    errorMessage.value = '所有字段均为必填项。';
    return;
  }
  
  try {
    const response = await axios.post(`${API_URL}/api/login`, form.value);
    if(response.data.success) {
      alert('登录成功！'); // In a real app, you would redirect or store the token
      errorMessage.value = '';
    }
  } catch (error) {
    console.error('Login failed:', error.response);
    // Display error from backend, or a generic one
    errorMessage.value = error.response?.data?.message || '登录失败，请重试。';
    // Refresh captcha on failed login attempt
    fetchCaptcha();
  }
};

onMounted(() => {
  fetchCaptcha();
});
</script>

<style scoped>
.login-card {
  display: flex;
  width: 800px;
  height: 450px;
  background-color: #1a1a2e;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  overflow: hidden;
}

/* Left Form Section */
.form-section {
  width: 50%;
  padding: 50px;
  color: #e0e0e0;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.form-group {
  margin-bottom: 25px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-size: 0.9rem;
  color: #a0a0a0;
}

.input-wrapper, .captcha-wrapper {
  display: flex;
  align-items: center;
  background-color: #2a2a3e;
  border: 1px solid #40405c;
  border-radius: 8px;
  padding: 0 15px;
}

.input-wrapper svg {
    color: #a0a0a0;
    margin-right: 10px;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  background: transparent;
  border: none;
  color: #fff;
  padding: 12px 0;
  font-size: 1rem;
}

input:focus {
  outline: none;
}

.captcha-wrapper input {
  flex-grow: 1;
}

.captcha-image {
  width: 100px;
  height: 40px;
  margin-left: 10px;
  border-radius: 5px;
  cursor: pointer;
}

.login-button {
  width: 100%;
  padding: 15px;
  border: none;
  border-radius: 8px;
  background-color: #007bff;
  color: #fff;
  font-size: 1.1rem;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-top: 10px;
}

.login-button:hover {
  background-color: #0056b3;
}

.error-message {
  color: #ff4d4d;
  text-align: center;
  margin-top: 15px;
  font-size: 0.9rem;
}

/* Right Illustration Section */
.illustration-section {
  width: 50%;
  background-color: #ffffff;
  padding: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.illustration-content {
    color: #333;
    text-align: center;
}

.illustration-content h2 {
    font-size: 1.8rem;
    font-weight: 500;
    margin-bottom: 10px;
}

.illustration-content p {
    color: #666;
    margin-bottom: 30px;
}

.illustration-image img {
    max-width: 100%;
    height: auto;
}
</style>
