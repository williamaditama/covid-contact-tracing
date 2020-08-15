import React from 'react';
import { View, Text, StyleSheet, ActivityIndicator } from 'react-native';
import MapView, { Marker } from 'react-native-maps'

import * as Location from 'expo-location'

import { getRiskLevel, postLocation } from '../services/httpRequests'


export default function MainScreen(props) {
    const [location, setLocation] = React.useState(null);
    const [errorMsg, setErrorMsg] = React.useState(null);
    const [riskLevel, setRiskLevel] = React.useState(null);



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

    let { latitude, longitude } = location.coords;
    // if (riskLevel === null) {
    getRiskLevel(latitude, longitude)
        .then(data => data.risk)
        .then(r => setRiskLevel(r))
    // }

    postLocation(latitude, longitude)
    .then(d => console.log(d));

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
        <Text>Risk Level:</Text>
        <Text>{riskLevel}</Text>
    </View>
}



const styles = StyleSheet.create({
    map: {
        width: '100%',
        height: 500
    },
    container: {
        margin: 24
    }
});