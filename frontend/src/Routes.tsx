import React, { FC } from 'react';
import { Switch, Route } from 'react-router-dom';
import { useHistory } from 'react-router';
import {
  Home,
  Login,
  SignUp,
  Protected,
  PrivateRoute,
  Documentation,
} from './views';
import { Admin } from './admin';
import { logout } from './utils/auth';
import Navigation from './components/Navigation';
export const Routes: FC = () => {
  const history = useHistory();

  return (
    <>
      <Navigation />
      <Switch>
        <Route path="/admin">
          <Admin />
        </Route>
        <div className={''}>
          <header className={''}>
            <Route path="/login" component={Login} />
            <Route path="/signup" component={SignUp} />
            <Route path="/docs" component={Documentation} />
            <Route
              path="/logout"
              render={() => {
                logout();
                history.push('/');
                return null;
              }}
            />
            <PrivateRoute path="/protected" component={Protected} />
            <Route exact path="/" component={Home} />
          </header>
        </div>
      </Switch>
    </>
  );
};
