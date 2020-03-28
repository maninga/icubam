import tornado
from tornado_sqlalchemy import SessionMixin

from backoffice.www.handlers.base import BaseBOHandler


class HomeBOHandler(SessionMixin, BaseBOHandler):
  ROUTE = '/'

  @tornado.web.authenticated
  def get(self):
    self.render("home.html")