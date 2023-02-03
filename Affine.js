class Rect {
    #key_order;
    constructor(key) {
        if (key.match(/[^A-Za-z]/)) {
            throw new Error("Key must only contain alphabet characters.");
        }
        if (key.split("").sort().join("").match(/(.)\1/)) {
            throw new Error("Key must avoid repeat characters.");
        }
        if (key.match(/[a-z]/)) {
            key = key.toUpperCase();
        }
        this.key = key;
        this.n = key.length;
        this.#key_order = [...key].sort().map(x => [...key].indexOf(x));
    }

    #encode(text) {
        return text.toUpperCase().replace(/[^A-Z]/g, "");
    }

    set_key(new_key) {
        this.__init__(new_key);
    }

    #pad(text, n) {
        let need_pad = -text.length % n;
        let pad = "";
        for (let i = 0; i < need_pad; i++) {
            pad += String.fromCharCode(Math.floor(Math.random() * 26) + 65);
        }
        return text + pad;
    }

    encrypt(text) {
        if (typeof text !== "string") {
            throw new TypeError("Input should be string");
        }
        text = this.#encode(text);
        text = this.#pad(text, this.n);
        let cipher = [];
        let text_list = [...text];
        for (let i = 0; i < text_list.length; i += this.n) {
            cipher.push(...this.#key_order.map(x => text_list[i + x]));
        }
        return [cipher.join(""), this.#key_order];
    }

    decrypt(text, key) {
        if (typeof text !== "string") {
            throw new TypeError("Input should be string");
        }
        if (text.length % this.n !== 0) {
            throw new Error(`The length of input should be a mutiple of ${this.n}`);
        }
        if (text.match(/[^A-Z]/)) {
            throw new Error("Invalid ciphertext: input contains non-alphabet characters");
        }
        let text_list = [...text];
        let plain_text = [];
        for (let i = 0; i < text_list.length; i += this.n) {
            plain_text.push(...this.#key_order.map(x => text_list[i + x]));
        }
        return plain_text.join("");
    }
}