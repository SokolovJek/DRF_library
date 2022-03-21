import React from 'react'
import {NavLink} from 'react-router-dom'


const ProjectItem = ({project}) => {
	return (
		<tr>
			<td>
				<NavLink to={`project/${project.uid}`}> {project.project_name} </NavLink>
			</td>
			<td>
				{project.users.map((user) => user + ', ')}

			</td>
			<td>
				{project.link_git}
			</td>
			<td>
				{project.descriptions}
			</td>
			<td>
				{project.date_create}
			</td>
		</tr>
		)
}


const ProjectsList = ({projects}) => {
    return(
        <table className='Table'>
            <tbody>
                <tr>
                    <th>
                            название проэкта
                    </th>
                    <th>
                        персонал
                    </th>
                    <th>
                        ссылка в git
                    </th>
                    <th>
                        описание
                    </th>
                    <th>
                        дата создания
                    </th>
                </tr>

                {projects.map((project) => <ProjectItem project={project}/>)}

            </tbody>
        </table>
	)
}

export default ProjectsList;