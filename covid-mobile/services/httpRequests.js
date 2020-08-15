import { AsyncStorage } from "react-native";

const URL = 'https://young-inlet-46417.herokuapp.com';


export async function postUser(userID) {
    return postRequest(URL + '/new_user', { userID })
}

export async function postLocation(lat, lng) {
    let userID = await AsyncStorage.getItem('userID');
    return postRequest(URL + '/new_location', { userID, lat, lng })
}

export async function getRiskLevel(lat, lng) {
    return postRequest(URL + '/risk_level', { lat, lng })
}


async function postRequest(url, body) {
    const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(body) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
}