import React from 'react';
import MainScreen from './screens/MainScreen';
import { AsyncStorage, ActivityIndicator } from 'react-native';

import { v4 as uuidv4 } from 'uuid';

import { postUser } from './services/httpRequests';

export default function App() {
  const [isLoading, setIsLoading] = React.useState(true);
  userSetup()
    .then(() => setIsLoading(false))
    .catch(() => setIsLoading(false)); // TODO Error message

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
    let userID = uuidv4();
    await AsyncStorage.setItem('userId', userID);
  }

  let isUserIdSent = await AsyncStorage.getItem('userIdSent');
  if (isUserIdSent === null) {
    let res = await postUser(userID); // TODO Send userID to server
    // TODO If res === HTTP OK
    await AsyncStorage.setItem('userIdSent', 'true');
  }
}