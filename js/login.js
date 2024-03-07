// login-form
const loginForm = document.getElementById('login-form');
const loginErrorMsg = document.getElementById('login-error-msg');
loginButton.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;
    // Request login
    // 使用post请求表单
    fetch('/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `username=${username}&password=${password}`
    }).then(res => {
        if (res.ok) {
            return res.json();
        }
    }).then(data => {
        if (data.status == 200) {
            const 登录密钥 = data.access_token
            window.localStorage.setItem('登录密钥', 登录密钥);
            window.location.href = '/';
        }
    })
})