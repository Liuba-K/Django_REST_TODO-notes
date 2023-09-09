import React from 'react';
import {Link} from 'react-router-dom';

const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td>
                <Link to={`project/${project.name_project}`}>{project.name_project}</Link>
            </td>
            <td>
                {project.users}
            </td>
            <td>
                <button onClick={()=>deleteProject(project.name_project)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const ProjectsList = ({projects, deleteProject}) => {
    return (
        <table>
            <th>
                Project name
            </th>
            <th>
                User
            </th>
            {projects.map((project) => <ProjectItem project={project}  deleteProject={ deleteProject}/>)}
            <th></th>
        </table>
    )
}

export default ProjectsList;
