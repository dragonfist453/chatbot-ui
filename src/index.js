import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

const chatApp = document.getElementById('chat-app');
ReactDOM.render(
    <React.Fragment>
        <App/>
    </React.Fragment>,
    chatApp
);