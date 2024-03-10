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
}

class Api{
    constructor(){
        this.auth_token = window.localStorage.getItem('Auth_Token');

    }
    static async post(url, data) {
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
    async check_login(){
        const response = await Api.post('/api/check_login', {});
        return response;
    }
}

const api = new Api();