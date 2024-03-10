// dom解析完成后执行
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const loginErrorMsg = document.getElementById('login-error-msg');
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const username = loginForm.username.value;
        const password = loginForm.password.value;
        // Request login
        // 使用post请求表单
        const req = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `username=${username}&password=${password}`
        })
        // 获取响应数据
        const res = await req.json();
        if (res.ok) {
            const data = res.json();
            // 处理响应数据
            const 登录密钥 = data.data.access_token
            console.log(登录密钥)
            window.localStorage.setItem('Auth_Token', 登录密钥);
            window.location.href = '/';
        }
    })
});