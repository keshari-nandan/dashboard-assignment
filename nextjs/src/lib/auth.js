

const isAutheitcated = async() => {
    const token = localStorage.getItem('token');
    const expiredIn = localStorage.getItem('expiredIn');
    return token && expiredIn > Date.now();
}

const setToken = async(token, expiresIn) => {
    localStorage.setItem('token', token);
    localStorage.setItem('expiredIn', Date.now() + expiresIn * 1000);
    await saveUser(token);
}

const saveUser = async(token) => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/users/me`, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    }).then((resp) => resp.json()).then((user) => localStorage.setItem('user', JSON.stringify(user)));
}

const getUser = async() => {
    return JSON.parse(localStorage.getItem('user'));
}

const getToken = async() => {
    return localStorage.getItem('token');
}

const removeToken = async() => {
    localStorage.removeItem('token');
    localStorage.removeItem('expiredIn');
}

export { isAutheitcated, setToken, removeToken, getUser, saveUser, getToken }