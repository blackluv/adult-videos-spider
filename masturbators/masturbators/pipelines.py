from scrapy.exceptions import DropItem

from models import *

class SaveVideoPipeline(object):
	def process_item(self, item, spider):
		video = Video()
		video.title = item.get("title")
		video.masturbator = spider.name
		video.remote_id = item.get("id")
		video.remote_url = item.get("url")
		video.remote_date = item.get("publish_date")
		video.duration = item.get("duration")

		db.session.add(video)
		db.session.commit()

		for tag_name in item.get("tags"):
				tag = VideoTag.query.filter_by(name=tag_name).first()

				if tag == None:
						tag = VideoTag()
						tag.name = tag_name

				video.tags.append(tag)

		for thumb_url in item.get("thumbs"):
				thumb = VideoThumb()
				thumb.url = thumb_url

				video.thumbs.append(thumb)

		for star_name in item.get("stars"):
				star = VideoStar.query.filter_by(name=star_name).first()

				if star == None:
						star = VideoStar()
						star.name = star_name

				video.stars.append(star)

		db.session.commit()

		raise DropItem()