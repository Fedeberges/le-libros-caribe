-- Le Libros Caribe — Schema PostgreSQL

CREATE TYPE subscription_tier AS ENUM ('free', 'premium', 'api');

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    subscription_tier subscription_tier DEFAULT 'free',
    stripe_customer_id VARCHAR(255),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    external_id VARCHAR(100) UNIQUE NOT NULL,
    source VARCHAR(50) NOT NULL,
    title VARCHAR(500) NOT NULL,
    author VARCHAR(500),
    language VARCHAR(10) DEFAULT 'en',
    subject VARCHAR(500),
    description TEXT,
    cover_url VARCHAR(500),
    file_url VARCHAR(500),
    amazon_url VARCHAR(500),
    download_count INT DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE user_library (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    book_id INT REFERENCES books(id) ON DELETE CASCADE,
    added_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, book_id)
);

CREATE TABLE annotations (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    book_id INT REFERENCES books(id) ON DELETE CASCADE,
    text TEXT NOT NULL,
    position VARCHAR(100),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Índices para búsqueda rápida
CREATE INDEX idx_books_title ON books USING gin(to_tsvector('spanish', title));
CREATE INDEX idx_books_author ON books(author);
CREATE INDEX idx_books_language ON books(language);
CREATE INDEX idx_books_source ON books(source);
