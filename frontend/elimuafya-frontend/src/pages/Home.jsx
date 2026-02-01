import "./Home.css";

const Home = () => {
  return (
    <section className="hero">
      {/* NAVBAR */}
      <nav className="navbar">
        <div className="logo">
          <span className="logo-icon">⚪</span>
          <span className="logo-text">ELIMUAFYA</span>
        </div>

        <div className="nav-links">
          <a href="#">Home</a>
          <a href="#">About</a>
          <a href="#">Contact</a>
        </div>

        <div className="auth-buttons">
          <a href="#" className="auth-link">
            Log in
          </a>
          <a href="#" className="auth-link primary">
            Sign up
          </a>
        </div>
      </nav>

      {/* HERO CONTENT */}
      <div className="hero-content">
        <div className="hero-text">
          <h1>
            Bridging Medical <br />
            Training With <br />
            Clinical Practice
          </h1>

          <a href="#" className="cta-btn">
            GET STARTED
          </a>
        </div>
      </div>
    </section>
  );
};

export default Home;
