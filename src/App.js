import React from 'react';
import { Widget, addResponseMessage} from "react-chat-widget";
import "react-chat-widget/lib/styles.css";
import "./style.css";
import axios from 'axios';

export default function App() {
    // Print hello in the beginning of the app
    React.useEffect(() => {
        addResponseMessage(`Hello!`)
    }, []);

    // Function to handle if a new message is added
    const handleNewUserMessage = (newMessage) => {
        getBotResponse(newMessage)
    };

    // Gets the response from python server using axios
    const getBotResponse = async (userMessage) => {
        await axios.post('http://localhost:5000/', `${userMessage}`)
            .then(res => {
                addResponseMessage(`${res.data}`)
            })
            .catch(err => {
                console.log(`Axios request failed: ${err}`)
            })
    }

    // Make the widget
    return (
        <div>
        <Widget
            title="Chatbot"
            subtitle=""
            handleNewUserMessage={handleNewUserMessage}
        />
        </div>
    );
}