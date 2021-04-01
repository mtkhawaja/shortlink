import React, { FC } from 'react';
import { Switch, Route } from 'react-router-dom';
import { useHistory } from 'react-router';
import { Redirector } from './components/Redirector';
import { Home, Login, SignUp, Documentation, NotFound404 } from './views';
import { Admin } from './admin';
import { logout } from './utils/auth';
import Navigation from './components/Navigation';

interface IPath {
  match: {
    url: string;
  };
}

function SiteRouter({ match }: IPath) {
  const history = useHistory();
  return (
    <>
      <Navigation />
      <Switch>
        <Route path={`${match.url}/admin`}>
          <Admin />
        </Route>
        <Route path={`${match.url}/login`} component={Login} />
        <Route
          path={`${match.url}/logout`}
          render={() => {
            logout();
            history.push('/');
            return null;
          }}
        />
        <Route path={`${match.url}/signup`} component={SignUp} />
        <Route path={`${match.url}/docs`} component={Documentation} />
        <Route path={`${match.url}/home`} component={Home} />
        <Route exact path={`${match.url}/`} component={Home} />
        <Route path="*" component={NotFound404} />
      </Switch>
    </>
  );
}

export const Routes: FC = () => {
  const history = useHistory();

  return (
    <>
      <Switch>
        <Route exact path="/:key_str" component={Redirector} />
        <Route path="/pages" component={SiteRouter} />
        <Route path="/*" component={SiteRouter} />
      </Switch>
    </>
  );
};
