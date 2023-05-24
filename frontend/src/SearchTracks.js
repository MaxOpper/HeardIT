import React, { useState } from 'react';

const SearchTracks = () => {
    const [query, setQuery] = useState('');
    const [tracks, setTracks] = useState([]);

    const searchTracks = async () => {
        const response = await fetch(`http://localhost:5000/api/search?q=${query}`);
        const data = await response.json();
        setTracks(data.tracks);
    };

    return (
        <div>
            <input 
                type="text" 
                placeholder="Search for a track" 
                value={query} 
                onChange={e => setQuery(e.target.value)}
            />
            <button onClick={searchTracks}>Search</button>
            <ul>
                {tracks.map((track, index) => (
                    <li key={index}>
                        {track.name} by {track.artist}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default SearchTracks;
