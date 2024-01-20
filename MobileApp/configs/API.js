import axios from "axios";

const host = "https://thanhduong.pythonanywhere.com"

export const endpoints = {
    'categories': '/categories/',
    'courses': '/courses/',

}

export const authApi = () => {
    return axios.create({
        baseURL: host,
        headers: {
            'Authorization': `Bearer ...`
        }
    })
}

export default axios.create({
    baseURL: host,
})