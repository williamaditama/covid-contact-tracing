import React from 'react';
import { View, Text, StyleSheet, ActivityIndicator } from 'react-native';
import MapView, { Marker } from 'react-native-maps'

import * as Location from 'expo-location'

import { getRiskLevel, postLocation } from '../services/httpRequests'

let globalLoc = null;

const INTERVAL_RISK = 1000;
const INTERVAL_LOC = 60000;

export default function MainScreen(props) {
    const [location, setLocation] = React.useState(null);
    const [errorMsg, setErrorMsg] = React.useState(null);
    const [riskLevel, setRiskLevel] = React.useState(null);
    const [isIntervalSetLoc, setIsIntervalSetLoc] = React.useState(false);
    const [isIntervalSetRisk, setIsIntervalSetRisk] = React.useState(false);

    if (!isIntervalSetRisk) {
        setInterval(() => {
            if (!globalLoc) return;
            let { latitude, longitude } = globalLoc.coords;
            getRiskLevel(latitude, longitude)
                .then(data => data.risk)
                .then(r => {
                    console.log("GETTING RISK", r)
                    setRiskLevel(r)
                })
        }, INTERVAL_RISK)
        setIsIntervalSetRisk(true);
    }
    if (!isIntervalSetLoc) {
        setInterval(() => {
            console.log('INTERVAL LOC')
            console.log(globalLoc)
            if (!globalLoc) return;
            let { latitude, longitude } = globalLoc.coords;
            postLocation(latitude, longitude)
                .then(d => console.log(d));
        }, INTERVAL_LOC)
        setIsIntervalSetLoc(true);
    }


    React.useEffect(() => {
        (async () => {
            let { status } = await Location.requestPermissionsAsync();
            if (status !== 'granted') {
                setErrorMsg('Permission to access location was denied');
            }

            let location = await Location.getCurrentPositionAsync({});
            setLocation(location);
        })();
    });


    let loc = 'Waiting..';
    if (errorMsg) {
        loc = errorMsg;
        return <View>
            <Text>Cannot Load Location</Text>
        </View>
    } else if (location) {
        loc = JSON.stringify(location);
    } else {
        return <View>
            <ActivityIndicator />
        </View>
    }
    console.log(loc)

    if (riskLevel === null) {
        let { latitude, longitude } = location.coords;
        getRiskLevel(latitude, longitude)
            .then(data => data.risk)
            .then(r => setRiskLevel(r))

        postLocation(latitude, longitude)
            .then(d => console.log(d));
    }

    // console.log('LOC', location)
    globalLoc = location;

    return <View style={styles.container}>
        <MapView style={styles.map}
            initialRegion={{
                latitude: location.coords.latitude,
                longitude: location.coords.longitude,
                latitudeDelta: 0.0922,
                longitudeDelta: 0.0421,
            }}
        >
            <Marker
                coordinate={location.coords}
                image={require('../assets/my-location.png')}
            />
        </MapView>
        <View style={styles.scoreCard}>
            <Text style={styles.label}>RISK LEVEL</Text>
            <Text style={{ ...styles.value, color: generateColor(riskLevel) }}>{riskLevel ? riskLevel.toFixed(2) : ''}</Text>
        </View>
    </View>
}

function generateColor(riskValue) {
    const MAX = 200
    const FROM = [7, parseInt('0xda'), parseInt('0x63')]
    const TO = [parseInt('0xe6'), parseInt('0x20'), parseInt('0x20')]
    let ret = []
    if (riskValue < MAX && riskValue >= 0) {
        let proportion = riskValue / MAX

        for (let i = 0; i < 3; i++) {
            let dif = TO[i] - FROM[i]
            ret.push(FROM[i] + proportion * dif)
        }
    } else {
        return '#000000'
    }
    let rv = ret.map(v => {
        return Math.round(v).toString(16)
    }).join('')
    rv = '#' + rv;
    return rv;
}


const styles = StyleSheet.create({
    map: {
        width: '100%',
        height: 500
    },
    container: {
        margin: 24
    },
    scoreCard: {
        margin: 8,
        padding: 4,
        elevation: 4,
        alignItems: 'center'
    },
    label: {
        color: '#777777'
    },
    value: {
        fontSize: 28
    }
})

