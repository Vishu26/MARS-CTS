import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Provider } from 'react-redux'
import store from './store'

import Header from './components/common/Header'
import Footer from './components/common/Footer'
import TravelForm from './components/Forms/TravelForm'
import CurrentLocation from './components/GoogleMap/CurrentLocation'

function App() {
  return (
    <Provider store={store}>
      <Router>
        <div className="App">
          <Header />

          <Switch>
            <Route exact path="/" component={TravelForm} />
            <Route exact path="/map" component={CurrentLocation} />
          </Switch>

          <Footer />
        </div>
      </Router>
    </Provider>
  );
}

export default App;
