import React, { Component } from 'react'
import { Map, GoogleApiWrapper } from 'google-maps-react';


class CurrentLocation extends Component {

    state = {}


    render() {
        const mapStyles = {
            width: '100%',
            height: '100%',
        };
        return (
            <div className="GoogleMaps">
                <Map
                    google={this.props.google}
                    zoom={8}
                    style={mapStyles}
                    initialCenter={{ lat: 47.444, lng: -122.176 }}
                />
            </div>
        )
    }
}

export default GoogleApiWrapper({
    apiKey: 'AIzaSyCfVJ5BempzSWsifnLXpNHwTAqh3lXL-oA'
})(CurrentLocation);

//export default CurrentLocation;