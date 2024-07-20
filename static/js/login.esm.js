import { utils } from './utils.esm.js';

function check_login() {
    // TODO
}

function login() {
    const loginForm = document.querySelector('#login-form');
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const username = loginForm.username.value;
        const password = loginForm.password.value;
        fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        })
            .then(res => res.json()).then(data => {
                console.debug(data)
                if (data.status == 200) {
                    const 登录密钥 = data.access_token
                    // 保存登录信息
                    window.localStorage.setItem('Auth_Token', 登录密钥);    
                    utils.toastify("success", "登录成功");
                    
                } else {
                    utils.toastify("error", "登录失败");
                }
            })
    });

}



export { login, check_login };

