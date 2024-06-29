import React from 'react';
import './About.css';

function About() {
    return (
        <div className="about-container">
            <h1>이 사이트에 관하여</h1>
            <p>
                위 네비게이션에서 library를 선택하면 도서관 정보를 검색하실 수 있는 사이트입니다. React를 기반으로
                만들었고 서울시 오픈 데이터를 사용했습니다.
            </p>
        </div>
    );
}

export default About;
