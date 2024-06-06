// src/components/Main.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import '../styles.css';

function Main() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        const initialPosts = [
            {
                title: '나의 첫번째 포스트',
                content: '반갑습니다! 아래의 사진들은 인류 지성사에 엄청난 족적을 남긴 거인들입니다.',
                images: [
                    'https://i.namu.wiki/i/ebctJN35Fc0wbutELVo9HnY0NJ8dq_TZW73pXYjki_DSBNiOZNdHzpKnSCaMaubjddt7wfPVN6heS_CXtwE-zA.webp',
                    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzrfl9W2xJiiQxJpG9CX2qosPpOawqsDA5vA&s',
                    'https://i.namu.wiki/i/_tRhuurPjMieMbxMUdXv71efn9L38blMJhIRivyebyAg_X9cTtHfYttNvpScLduUSP3LKJfveu6LA1SzojY0qQ.webp',
                ],
            },
            // 추가 포스트들...
        ];

        if (!localStorage.getItem('posts')) {
            localStorage.setItem('posts', JSON.stringify(initialPosts));
        }

        const storedPosts = JSON.parse(localStorage.getItem('posts')) || [];
        setPosts(storedPosts);
    }, []);

    return (
        <div>
            <h1>메인 페이지</h1>
            <div>
                {posts.map((post, index) => (
                    <div key={index}>
                        <h2>{post.title}</h2>
                        <p>{post.content}</p>
                        {post.images.map((image, imgIndex) => (
                            <img
                                key={imgIndex}
                                src={image}
                                alt={`Post ${index} - Image ${imgIndex}`}
                                className="responsive"
                            />
                        ))}
                        <Link to={`/detail/${index}`}>Read More</Link>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Main;
