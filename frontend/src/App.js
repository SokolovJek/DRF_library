import './App.css';
import React from 'react';
import AuthorList from './components/Author.js'
import axios from 'axios'
import ProjectsList from './components/Project.js'
import TodosList from './components/Todo.js'
import ProjectsTodo from './components/ProjectTodo.js'
import {HashRouter, Route, NavLink, Switch, Redirect} from 'react-router-dom'
import LoginForm from './components/Auth.js'
import Cookies from 'universal-cookie'


const page_not_found_404 = function(location){
    return(
        <div>
            <h1>К сожалению данная страница '{location.pathname}' отсутствует, проверте корректность указаного адреса.</h1>
        </div>
    )
}




class App extends React.Component {
	constructor(props) {
		super(props)
		this.state = {
			'authors': [],
			'projects': [],
			'todos': [],
			'token': '',
		}
	}

	set_token(token){
	    const cookies = new Cookies()
	    cookies.set('token', token)
	    this.setState({'token': token}, () => this.load_data())
	    }


    get_token_from_storage(){
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated(){
        return this.state.token != ''
    }

    logout(){
        this.set_token('')
    }

	get_token(username, password){
	    console.log(username + ' ' + password)
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username:username, password:password})
        .then(response => {
            this.set_token(response.data['token'])
            })
        .catch(error => alert('Неверный логин или пароль'))
    }

    get_headers(){
        let headers = {'Content-Type': 'application/json'}
        if (this.is_authenticated())
        {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        console.log(headers)
        return headers
    }


    load_data(){
        const headers = this.get_headers()

        axios.get('http://127.0.0.1:8000/api/author/', {headers})
			.then(response => {
				const authors = response.data
				this.setState(
					{ 'authors': authors }
				)
			}).catch(error => {console.log('--my--error-' + error)
			                   this.setState({authors: []})
			 })


		axios.get('http://127.0.0.1:8000/api/projects/', {headers})
			.then(response => {
				const projects = response.data
				this.setState(
					{ 'projects': projects }
				)
			}).catch(error => {console.log('--my--error-' + error)
			                   this.setState({projects: []})
			 })


	    axios.get('http://127.0.0.1:8000/api/todo/', {headers})
			.then(response => {
				const todos = response.data
				this.setState(
					{ 'todos': todos }
				)
			}).catch(error => {console.log('--my--error-' + error)
			                   this.setState({todos: []})
			 })

    }


	componentDidMount() {
		this.get_token_from_storage()

	}


	render() {
		return (
			<div className='container header'>

                <HashRouter>

                    <nav>
                        <ul>
                            <li>
                                <NavLink to='/'> список пользователей</NavLink>
                            </li>
                            <li>
                                <NavLink to='/projects'> проэкты </NavLink>
                            </li>
                            <li>
                                <NavLink to='/todos'> todo </NavLink>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}> logout </button> :
                                    <NavLink to='/login'> login </NavLink>}
                            </li>
                        </ul>
                    </nav>

                    <div className='row'>
                        <div className='col-12'>
                            <h1 className='text-center text-white'>
                                Всz информация
                            </h1>
                            <a href='http://127.0.0.1:8000/api/author/' className='btn itd_play text-uppercase'>Перейти</a>
                        </div>

                    </div>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors} /> } />
                        <Route exact path='/projects' component={() => <ProjectsList projects={this.state.projects} /> } />
                        <Route exact path='/todos' component={() => <TodosList todos={this.state.todos} /> } />
                        <Route path='/project/:id' component={() => <ProjectsTodo projects={this.state.projects}/> } />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username,
                            password) => this.get_token(username, password)} /> } />
                        <Redirect from='/authors' to='/' />
                        <Route component={page_not_found_404} />

                    </Switch>



                </HashRouter>
			</div>

		)

	}
}


export default App;
