import React from 'react';
import MainScreen from './screens/MainScreen';
import { AsyncStorage, ActivityIndicator } from 'react-native';

import { v4 as uuidv4 } from 'uuid';

export default function App() {
  const [isLoading, setIsLoading] = React.useState(true);
  userSetup().then(() => setIsLoading(false));

  if (isLoading)
    return <ActivityIndicator />
  return (
    <MainScreen />
  );
}


async function userSetup() {
  // Store new user if not created already
  let storedID = await AsyncStorage.getItem('userId');
  if (storedID === null) {
    await AsyncStorage.setItem('userId', uuidv4());
  }

  let isUserIdSent = await AsyncStorage.getItem('userIdSent');
  if (isUserIdSent === null) {
    let res = await fetch(); // TODO Send userID to server
    // TODO If res === HTTP OK
    await AsyncStorage.setItem('userIdSent', 'true');
  }
}