import { utils } from './utils.esm.js';
import * as login_api from './login.esm.js';

document.addEventListener("DOMContentLoaded", async (e) => {
    console.debug("DOM 加载完成");
    utils.hide_page_loading()
    try {
        utils.show_loading()
        let res = await login_api.check_login()
        utils.hide_loading()
        if (res.username) {
            // 已登录
            console.log(res);
        } else {
            console.log("未登录");
            login_api.show_login()
        }
    } catch (e) {
        utils.hide_loading()
        console.error(e)
    }

})
