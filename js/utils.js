class Utils {
    static toastify(type, message, options) {
        let options = {
            text: message,
            duration: 3000,
            close: true,
            gravity: "top",
            position: "right",
            stopOnFocus: true,
            className: `toastify-${type}`,
            ...options
        };
        Toastify(options).showToast();
    }
    static async post(url, data) {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'

            },
            body: JSON.stringify(data)
        })
        return response.json()
    }
}

utils = new Utils()