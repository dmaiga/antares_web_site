# Antares Web Application

## Description
Antares is a corporate web application under development for Antares, a human resources consulting firm. This project is currently in the construction phase, focusing on building the static components of the corporate website. The dynamic functionalities will be implemented in future phases.

## Current Phase
- **Status**: Static web development
- **Focus**: Creating the corporate website's static pages and layout
- **Dynamic Features**: Not implemented yet

## Project Structure
The project is organized as follows:

```
antares_web/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py

site_web/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    urls.py
    views.py
    migrations/
        __init__.py
    static/
        images/
            clients/
            espaces/
            favicon/
                site.webmanifest
            home/
            logo/
            services/
    templates/
        base.html
        site_web/
            about/
                about.html
                partials/
                    _cta_about.html
                    _history.html
                    _secteur.html
                    _services.html
                    _values.html
            auth/
                login.html
                register.html
            contact/
                contact.html
            espaces/
                espace_candidat.html
                espace_consultant.html
                espace_entreprise.html
                partials/
                    candidat/
                        _forms.html
                        _hero_section.html
                        _step.html
                        _why_join.html
                    consultant/
                        _enrollment_form.html
                        _hero_section.html
                        _why_join_us.html
                    entreprise/
                        _clients.html
                        _enroulement_form.html
                        _hero.html
                        _services_grid.html
                        _stats.html
                        _steps_recruteur.html
            home/
                home.html
                partials/
                    _cta_section.html
                    _job_offers_list.html
                    _profils.html
            jobs/
                detail_job.html
                jobs.html
                partials/
                    _cta.html
                    _job_card.html
                    _job_empty_state.html
                    _job_filters.html
                    _job_hero.html
                    _job_pagination.html
                    _sidebar_ad.html
                    _special_offer_card.html
            partials/
                _footer.html
                _language_switcher.html
                _navbar.html
            services/
                savoir_plus.html
                services.html
                partials/
                    _card_services.html
                    _hero.html
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/dmaiga/antares_web_site.git
   ```
2. Navigate to the project directory:
   ```bash
   cd antares_web
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```
5. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Future Plans
- Implement dynamic features such as user authentication, job postings, and application management.
- Enhance the design and responsiveness of the website.
- Deploy the application to a production environment.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
