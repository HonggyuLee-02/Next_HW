// src/components/Detail.js
import React, { useEffect, useState, useRef } from 'react';
import { useParams } from 'react-router-dom';
import '../styles.css';

function Detail() {
    const { id } = useParams();
    const [post, setPost] = useState(null);
    const imgRefs = useRef([]);

    useEffect(() => {
        const storedPosts = JSON.parse(localStorage.getItem('posts')) || [];
        const currentPost = storedPosts[id];
        setPost(currentPost);
    }, [id]);

    const handleImageClick = (index) => {
        if (imgRefs.current[index]) {
            imgRefs.current[index].src = 'https://via.placeholder.com/150'; // 예시 URL, 원하는 URL로 바꿔주세요.
        }
    };

    if (!post) return <div>Loading...</div>;

    return (
        <div>
            <h1>{post.title}</h1>
            <p>{post.content}</p>
            {post.images.map((image, index) => (
                <img
                    key={index}
                    src={image}
                    alt={`Detail Image ${index}`}
                    onClick={() => handleImageClick(index)}
                    ref={(el) => (imgRefs.current[index] = el)}
                    className="responsive" // CSS 클래스 추가
                />
            ))}
        </div>
    );
}

export default Detail;
