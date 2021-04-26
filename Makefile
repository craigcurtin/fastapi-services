test:
	run pytest

create-items:
	curl -X POST localhost:7000/foo/item/   --data '{"description":"some item a, description", "public":false}' --verbose
	curl -X POST localhost:7000/foo/item/   --data '{"description":"some item b,  description", "public":false}' --verbose
	curl -X POST localhost:7000/foo/item/   --data '{"description":"some item c,  description", "public":false}' --verbose
	curl -X POST localhost:7000/foo/item/   --data '{"description":"some item A,  description", "public":true}' --verbose
	curl -X POST localhost:7000/foo/item/   --data '{"description":"some item B,  description", "public":true}' --verbose
	curl -X POST localhost:7000/foo/item/   --data '{"description":"some item C,  description", "public":true}' --verbose
	curl -X POST localhost:7000/foo/item/   --data '{"description":"some item D,  description", "public":true}' --verbose

get-items:
	curl -X GET localhost:7000/foo/item/1 --verbose
	curl -X GET localhost:7000/foo/item/2 --verbose
