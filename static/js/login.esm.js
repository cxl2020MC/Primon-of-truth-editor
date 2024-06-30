import {utils} from './utils.esm.js';

// dom解析完成后执行
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.querySelector('#login-form');
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const username = loginForm.username.value;
        const password = loginForm.password.value;
        // Request login
        // 使用post请求表单
        axios.post('/api/login', {
                username: username,
                password: password
        })
        .then(res => {
            console.log(res)
            // 处理响应数据
            if (res.status == 200) {
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
        .catch(err => {
        })
    })
})