from django.utils import timezone

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    new_movie_session = MovieSession(show_time=movie_show_time)

    if movie_id:
        movie = Movie.objects.get(pk=movie_id)
        new_movie_session.movie = movie

    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
        new_movie_session.cinema_hall = cinema_hall

    new_movie_session.save()
    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()

    if session_date:
        date = timezone.datetime.strptime(session_date, "%Y-%m-%d").date()
        queryset = queryset.filter(show_time__date=date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(pk=session_id)

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie = Movie.objects.get(pk=movie_id)
        movie_session.movie = movie

    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
        movie_session.cinema_hall = cinema_hall

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(pk=session_id).delete()
