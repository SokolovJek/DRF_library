import './App.css';
import React from 'react';
import AuthorList from './components/Author.js'
import axios from 'axios'
import ProjectsList from './components/Project.js'
import TodosList from './components/Todo.js'
import ProjectsTodo from './components/ProjectTodo.js'
import {HashRouter, Route, NavLink, Switch, Redirect} from 'react-router-dom'


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
			'projects':[],
			'todos':[]
		}
	}

	componentDidMount() {
		axios.get('http://127.0.0.1:8000/api/author/')
			.then(response => {
				const authors = response.data
				console.log('-----------my-----response----------------' + response.data)
				this.setState(
					{ 'authors': authors }
				)
			}).catch(error => console.log('-----------my-----error----------------' + error))


		axios.get('http://127.0.0.1:8000/api/projects/')
			.then(response => {
				const projects = response.data
				console.log('-----------my-----response----------------' + response.data)
				this.setState(
					{ 'projects': projects }
				)
			}).catch(error => console.log('-----------my-----error----------------' + error))



	    axios.get('http://127.0.0.1:8000/api/todo/')
			.then(response => {
				const todos = response.data
				console.log('-----------my-----response----------------' + response.data)
				this.setState(
					{ 'todos': todos }
				)
			}).catch(error => console.log('-----------my-----error----------------' + error))

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
                        </ul>
                    </nav>

                    <div className='row'>
                        <div className='col-12'>
                            <h1 className='text-center text-white'>
                                Все пользователи с сайта
                            </h1>
                            <a href='http://127.0.0.1:8000/api/author/' className='btn itd_play text-uppercase'>Перейти</a>
                        </div>

                    </div>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors} /> } />
                        <Route exact path='/projects' component={() => <ProjectsList projects={this.state.projects} /> } />
                        <Route exact path='/todos' component={() => <TodosList todos={this.state.todos} /> } />

                        <Route path='/project/:uid' component={() => <ProjectsTodo projects={this.state.projects}/> } />

                        <Redirect from='/authors' to='/' />
                        <Route component={page_not_found_404} />

                    </Switch>



                </HashRouter>
			</div>

		)

	}
}


export default App;
