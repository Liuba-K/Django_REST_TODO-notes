import axios from 'axios';
import './App.css';
import React from 'react';
import UserList from './components/User.js';
import Footer from './components/Footer.js';
import Menu from './components/Menu.js';


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
                this.setState(
                    {
                        'users': response.data
                    }
                )
        }).catch(error => console.log(error))
    }
    render(){
            return (
                <div>
                    <Menu />
                    <UserList users={this.state.users} />
                    <Footer />
                 </div>
            )
        }
}

export default App;


