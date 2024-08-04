
class utils {
    static toastify(type, message, options) {
        let toastify_options = {
            text: message,
            duration: 3000,
            close: true,
            gravity: "top",
            position: "right",
            stopOnFocus: true,
            className: `toastify-${type}`,
            ...options
        };
        Toastify(toastify_options).showToast();
    }
    static hide_page_loading() {
        const page_loading_div = document.getElementById('page_loading_magisk');
        page_loading_div.classList.remove('show');
        page_loading_div.classList.add('hide');
    }
    static show_page_loading() {
        const page_loading_div = document.getElementById('page_loading_magisk');
        page_loading_div.classList.remove('hide');
        page_loading_div.classList.add('show');
    }
    static show_loading() {
        const loading_div = document.getElementById('loading_div');
        loading_div.classList.remove('hide');
        loading_div.classList.add('show');
    }
    static hide_loading() {
        const loading_div = document.getElementById('loading_div');
        loading_div.classList.remove('show');
        loading_div.classList.add('hide');
    }
}


class api{
    constructor(){
        this.auth_token = window.localStorage.getItem('Auth_Token');
    }
    async post(url, data) {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${this.auth_token}`
            },
            body: JSON.stringify(data)
        })
        return response.json()
    }
    async get(url) {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${this.auth_token}`
            },
        })
        return response.json()
    }
    async check_login(){
        const response = await this.get('/api/check_login', {});
        return response;
    }
    async get_juqin(){
        const response = await this.get('/api/get_juqin', {});
        return response;
    }
}

const Utils = new utils();
const Api = new api();

export { Utils, Api };