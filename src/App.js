import React from 'react';
import { Widget, addResponseMessage, addUserMessage } from "react-chat-widget";
import "react-chat-widget/lib/styles.css";
import "./style.css";

export default function App() {
  const [messages, newMessages] = React.useState({
    user: '',
    bot: "Hello"
  });

  React.useEffect(() => {
    let {user, bot} = messages;
    if (bot !== "") addResponseMessage(bot);
    if (user !== "") addUserMessage(user);
  }, []);
  const handleNewUserMessage = (newMessage) => {
    newMessages({...messages, user: `${newMessage}`});
    // Now send the message throught the backend API
  };
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