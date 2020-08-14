import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import MapView from 'react-native-maps'


export default function MainScreen(props) {

    return <View style={styles.container}>
        <MapView style={styles.map}
            initialRegion={{
                latitude: 6.2088,
                longitude: -106.8456,
                latitudeDelta: 0.0922,
                longitudeDelta: 0.0421,
            }}
        />
        <Text>COVID Score:</Text>
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