import axios from 'axios';
import './App.css';
import React from 'react';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import TodoList from './components/Todo.js';
import Footer from './components/Footer.js';
import Menu from './components/Menu.js';
import {BrowserRouter,Route,Routes,Link,Navigate} from 'react-router-dom';


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos' : [],
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

                        <BrowserRouter>
                            <nav>
                                <li>
                                    <Link to='/users'>Users</Link>
                                </li>
                                <li>
                                    <Link to='/projects'>Projects</Link>
                                </li>
                                <li>
                                    <Link to='/todos'>Todos</Link>
                                </li>
                            </nav>
                            <Menu />
                            <Routes>
                                <Route exact path='/users' element={<UserList users={this.state.users} />}/>
                                <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />}/>
                                <Route exact path='/todos' element={<TodoList todos={this.state.todos} />}/>
                            </Routes>
                        </BrowserRouter>
                    <Footer />
                 </div>
            )
        }
}

export default App;


