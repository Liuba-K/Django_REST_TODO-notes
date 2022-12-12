import React from 'react';
import {Link} from 'react-router-dom';

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                <Link to={`project/${project.name_project}`}>{project.name_project}</Link>
            </td>
            <td>
                {project.users}
            </td>
        </tr>
    )
}

const ProjectsList = ({projects}) => {
    return (
        <table>
            <th>
                Project name
            </th>
            <th>
                User
            </th>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectsList;
