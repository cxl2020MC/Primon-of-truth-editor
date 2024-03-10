// dom解析完成后执行
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.querySelector('#login-form');
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
        const res = await req.json();
        // 处理响应数据
        if (res.code == 200) {
            const 登录密钥 = res.data.access_token
            // 保存登录信息
            window.localStorage.setItem('Auth_Token', 登录密钥);
            utils.toastify("success", "登录成功");
            // 跳转到主页
            setTimeout(() => {
                window.location.href = '/';
            }, 1000);
        } else {
            utils.toastify("error", res.msg);
        }

    })
});