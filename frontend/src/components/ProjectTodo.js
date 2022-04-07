import React from 'react'
import {useParams} from 'react-router-dom'


const ProjectTodo = ({project}) => {
	return (
		<tr>
		    <td>
				{project.project_name}
			</td>
			<td>
				{project.descriptions}
			</td>
			<td>
				{project.users.map((user) => user + ', ')}
			</td>
			<td>
				{project.link_git}
			</td>
			<td>
				{project.date_create}
			</td>
			<td>
				{project.set_todo.map((project) => project + '; ')}
			</td>
		</tr>
		)
}


const ProjectsTodo = ({projects}) => {
    let {id} = useParams()         // можно так
//    let my_id = useParams().id    // но так наглядней
    let filter_project = projects.filter((project) => project.id == id)
    return(
        <table className='Table'>
            <tbody>
                <tr>
                    <th>
                            название проэкта
                    </th>
                    <th>
                        описание
                    </th>
                    <th>
                    персонал

                    </th>
                    <th>
                        ссылка в git
                    </th>
                    <th>
                        дата создания
                    </th>
                    <th>
                        список ToDo
                    </th>
                </tr>

                {filter_project.map((project) => <ProjectTodo project={project}/>)}

            </tbody>
        </table>
	)
}

export default ProjectsTodo;