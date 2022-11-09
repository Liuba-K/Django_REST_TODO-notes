
import './App.css';
import React from 'react';
import UserList from './components/User.js'


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
    const users = [
        {
            'firstname': 'Фёдор',
            'lastname': 'Нагорный',
            'birthday_year': 1921
        },
        {
            'firstname': 'Александр',
            'lastname': 'Грин',
            'birthday_year': 1980
        },
    ]
    this.setState(
        {
        'users': users
        }
        )
    }

    render () {
      return (
          <div>
            <UserList users={this.state.users} />
           </div>
       )
     }
}

export default App;
