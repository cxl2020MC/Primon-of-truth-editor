import { utils, Api } from "./utils.esm.js";

async function check_login() {
    // const res = await fetch("/api/check_login", { method: "GET" });
    const res = await Api.get("/api/check_login");
    if (res.status == 200) {
        console.debug("已登录");
    };
    const data = res.json();
    return data;
};

function login() {
    const loginForm = document.querySelector("#login-form");
    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        // const username = loginForm.username.value;
        // const password = loginForm.password.value;
        const req_body = new FormData(loginForm);
        fetch("/api/login", {
            method: "POST",
            // headers: {
                // "Content-Type": "application/json",
            // },
            // body: JSON.stringify({
                // username: username,
                // password: password,
            // }),
            body: req_body
        })
            .then((res) => res.json())
            .then((data) => {
                console.debug(data);
                if (data.status == 200) {
                    const 登录密钥 = data.access_token;
                    // 保存登录信息
                    window.localStorage.setItem("Auth_Token", 登录密钥);
                    utils.toastify("success", "登录成功");
                    // 关闭登录窗口

                } else {
                    utils.toastify("error", "登录失败");
                }
            });
    });
}

function show_login() {
    // 页面最后插入登录容器
    const HTML = `
    <dialog id="login">
        <form id="login-form">
            <h2>登录</h2>
            <input type="text" id="username" name="username" placeholder="用户名">
            <input type="password" id="password" name="password" placeholder="密码">
            <input type="submit" value="登录">
        </form>
    </dialog>`;
    document.body.insertAdjacentHTML("beforeend", HTML);
    const login = document.querySelector("#login");
    login.showModal();
    login();
}

function hide_login() {
    const login = document.querySelector("#login");
    login.close();
}


export { login, check_login, show_login };
