import axios from 'axios';
import './App.css';
import React from 'react';

import UserList from './components/User.js';
import ProjectList from './components/OneProject.js';
import ProjectsList from "./components/Project.js";
import TodoList from './components/Todo.js';

import Footer from './components/Footer.js';
import Menu from './components/Menu.js';
import NotFound404 from './components/NotFound404';

import LoginForm from './components/Auth';
import todos from "./components/Todo";
import TodoForm from "./components/TodoForm";
import {BrowserRouter,Route,Routes,Link,Navigate} from 'react-router-dom';

import Cookies from 'universal-cookie';


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token':'',
        }
    }

    create_todo(text, users){
        const headers = this.get_headers()
        const data = {text: text, users: users}
        axios.post(`http://127.0.0.1:8000/api/todos/`, data, {headers}).then(response => {
            this.load_data()
        }).catch(error => {
            console.log(error)
            this.setState({todos:[]})
            })
    }

    delete_todo(user){
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todos/${user}`, {headers}).then(response => {
            //this.setState(
            //    {
            //    'todos': response.data
            //    }
            //)
            this.load_data()
        }).catch(error => {
            console.log(error)
            this.setState({todos:[]})})
    }

    logout(){
        this.set_token('')
        this.setState({'users':[]})

    }

    is_auth(){
        return !!this.state.token

    }

    set_token(token){
        console.log(token)
        const cookies = new Cookies()
        cookies.set('token',token)
        this.setState({'token':token}, () => this.load_data())

    }

    get_token_storage(){
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token':token},() => this.load_data())

    }

    get_token(username, password){
        const data = {username:username,password:password}
        axios.post('http://127.0.0.1:8000/api-token-auth/',data).then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))

        //console.log(username,password)

    }

    get_headers(){
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_auth()){
            headers['Authorization'] = 'Token '+this.state.token
        }
        return headers
    }

    load_data(){
    //}
    //componentDidMount() {
        const headers = this.get_headers() //!!внимательно
        axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(response => {
                this.setState(
                    {
                        'users': response.data
                    }
                )
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/',  {headers}).then(response => {
                this.setState(
                    {
                        'projects': response.data
                    }
                )
        }).catch(error => console.log(error))

         axios.get('http://127.0.0.1:8000/api/todos/', {headers}).then(response => {
                this.setState(
                    {
                        'todos': response.data
                    }
                )
        }).catch(error => console.log(error))

    }
    componentDidMount() {
        this.get_token_storage()
    }

    render(){
            return (
                <div>
                        <Menu />
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
                                <li>
                                    {this.is_auth() ? <button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                                </li>
                            </nav>

                            <Routes>
                                <Route exact path='/' element={<Navigate to='/projects'/>}/>
                                <Route path = '/projects'>
                                    <Route index element={<ProjectsList projects={this.state.projects} />}/>
                                    <Route path='/projects/:name_project' element={<ProjectList projects={this.state.projects} />}/>
                                 </Route>
                                <Route exact path='/users' element={<UserList users={this.state.users} />}/>

                                <Route exact path='/todos' element={<TodoList todos={this.state.todos}  delete_todo={(user)=>this.delete_todo(user)}/>}/>
                                <Route exact path='/todos/create'
                                    element={<TodoForm todos={this.state.todos}
                                        create_todo={(text, users)=>this.create_todo(text, users)}/>}/>

                                <Route exact path='/login' element={<LoginForm get_token={(username,password) =>
                                this.get_token(username,password)} />}/>

                                <Route path='*' element={<NotFound404/>}/>
                            </Routes>
                        </BrowserRouter>
                        <Footer />

                 </div>
            )
        }
}

export default App;


